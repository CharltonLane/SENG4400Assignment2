'use strict';

window.addEventListener('load', function () {

    console.log("Hello World!");

});

const apiEndpoint = "/getNewEntries"
const apiEndpointGet50 = "/get50Entries"

const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        content: []
    },
    created (){
        this.fetchLast50Entries();
        this.timer = setInterval(this.fetchNewEntries, 1000);
    },
    methods: {
        async fetchNewEntries () {
            const gResponse = await fetch(apiEndpoint);
            const gObject = await gResponse.json();
            console.log("Got this: " + JSON.stringify( gObject));
            this.content = this.content.concat(gObject["data"]);
        },
        async fetchLast50Entries () {
            const gResponse = await fetch(apiEndpointGet50);
            const gObject = await gResponse.json();
            console.log("Got this last 50: " + JSON.stringify( gObject));
            this.content = gObject["data"];
        }
    }

})


const generate10NewItems = async () => {
  const response = await fetch('https://australia-southeast1-c3299743seng4400a2.cloudfunctions.net/SENG4400Server');
}