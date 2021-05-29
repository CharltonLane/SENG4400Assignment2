'use strict';

const apiEndpoint = "/getNewEntries"
const apiEndpointGet50 = "/get50Entries"
const apiEndpointClearEntries = "/clearAllEntries"

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
            console.log("Got this many results: " + gObject["data"].length);


            // Update the lastAnswerCreationTime to about ten seconds ago.
            this.lastAnswerCreationTime = new Date().getTime() - 10000;

            // Only add new results.
            for (let i=0; i < gObject["data"].length; i++){
                console.log("Ah")
                if(!this.content.some(entry => entry.question === gObject["data"][i].question)){
                    console.log("Pushed " + gObject["data"][i].question)
                    this.content.push(gObject["data"][i]);
                }
            }

            // Remove the oldest results if we have 50 answers.
            if (this.content.length >= 50) {
                for (let i = 0; i < this.content.length-50; i++){
                    this.content.shift();
                }
            }

        },
        async fetchLast50Entries () {
            const gResponse = await fetch(apiEndpointGet50);
            const gObject = await gResponse.json();
            //console.log("Got this last 50: " + JSON.stringify( gObject));
            this.content = gObject["data"];
        },

    }

})

const clearAllEntries = async () => {
    await fetch(apiEndpointClearEntries);
    vm.content = [];
}

const generate50NewItems = async (cloudFunction) => {
    for (let i=0; i < 50; i++) {
        const response = await fetch('https://australia-southeast1-seng4400c3299743.cloudfunctions.net/' + cloudFunction);
    }
}

const generate1NewItem = async (cloudFunction) => {
    console.log("Asked for a new result")
    const response = await fetch('https://australia-southeast1-seng4400c3299743.cloudfunctions.net/' + cloudFunction);
    console.log(response)
}