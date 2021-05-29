'use strict';

const apiEndpoint = "/getNewEntries"
const apiEndpointGet50 = "/get50Entries"
const apiEndpointClearEntries = "/clearAllEntries"

const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        content: [],
        lastAnswerCreationTime: new Date().getTime(),
        isLoading: true
    },
    created() {
        this.fetchLast50Entries();
        this.timer = setInterval(this.fetchNewEntries, 1000);
    },
    methods: {
        async fetchNewEntries() {
            //console.log("gug" + this.lastAnswerCreationTime);

            const response = await fetch(apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json;charset=utf-8'
                },
                body: JSON.stringify({
                    "lastCheckDate": this.lastAnswerCreationTime
                })
            })
            const responseJSON = await response.json();
            const newEntries = responseJSON["data"];

            //console.log("Got this: " + JSON.stringify( newEntries));
            console.log("Got this many results: " + newEntries.length);

            // Update the lastAnswerCreationTime to about ten seconds ago.
            this.lastAnswerCreationTime = new Date().getTime() - 10000;

            // Only add new results.
            for (let i = 0; i < newEntries.length; i++) {
                console.log("Ah" + newEntries[i].time_generated)
                if (!this.content.some(entry => entry.question === newEntries[i].question && entry.time_generated === newEntries[i].time_generated)) {
                    console.log("Pushed " + newEntries[i].question)
                    newEntries[i].expanded = false;
                    this.content.push(newEntries[i]);
                    vm.isLoading = false;
                }
            }

            // Remove the oldest results if we have 50 answers.
            if (this.content.length >= 50) {
                for (let i = 0; i < this.content.length - 50; i++) {
                    this.content.shift();
                }
            }


        },
        async fetchLast50Entries() {
            const gResponse = await fetch(apiEndpointGet50);
            const gObject = await gResponse.json();
            //console.log("Got this last 50: " + JSON.stringify( gObject));
            this.content = gObject["data"];
            for (let i=0; i < this.content.length; i++){
                this.content[i].expanded = false;
            }

            vm.isLoading = false;
        },
    }
})

const clearAllEntries = async () => {
    vm.isLoading = true;
    await fetch(apiEndpointClearEntries);
    vm.content = [];
    vm.isLoading = false;
}

const generate50NewItems = async (maxRandomNumber) => {
    vm.isLoading = true;
    for (let i = 0; i < 50; i++) {
        await generate1NewItem(maxRandomNumber);
    }
}

const generate1NewItem = async (maxRandomNumber) => {
    vm.isLoading = true;
    await fetch('https://australia-southeast1-seng4400c3299743.cloudfunctions.net/ServerSingle', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({
            "MAX_RANDOM_NUMBER": maxRandomNumber
        })
    });
}