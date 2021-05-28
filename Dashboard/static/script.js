'use strict';

const apiEndpoint = "/getNewEntries"
const apiEndpointGet50 = "/get50Entries"

const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        content: [],
        lastAnswerCreationTime: new Date().getTime()
    },
    created (){
        this.fetchLast50Entries();
        this.timer = setInterval(this.fetchNewEntries, 1000);
    },
    methods: {
        async fetchNewEntries () {
            //console.log("gug" + this.lastAnswerCreationTime);

            const gResponse = await fetch(apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify({
                    "lastCheckDate": this.lastAnswerCreationTime
                }) // The data
            });

            const gObject = await gResponse.json();
            //console.log("Got this: " + JSON.stringify( gObject));

            // Update the lastAnswerCreationTime.
            this.lastAnswerCreationTime = new Date().getTime();

            // Remove the oldest results if we have 50 answers.
            if (this.content.length >= 50) {
                for (let i = 0; i < gObject["data"].length; i++){
                    this.content.shift();
                }
            }

            // Add this result to the end of the list.
            this.content = this.content.concat(gObject["data"]);
        },
        async fetchLast50Entries () {
            const gResponse = await fetch(apiEndpointGet50);
            const gObject = await gResponse.json();
            //console.log("Got this last 50: " + JSON.stringify( gObject));
            this.content = gObject["data"];
        }
    }

})


const generate10NewItems = async () => {
  const response = await fetch('https://australia-southeast1-c3299743seng4400a2.cloudfunctions.net/SENG4400Server');
}