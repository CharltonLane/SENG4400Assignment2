'use strict';

const apiEndpointGetRecent = "/getNewEntries"
const apiEndpointGet50 = "/get50Entries"
const apiEndpointClearEntries = "/clearAllEntries"

const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        content: [],
        isLoading: true
    },
    created() {
        // These functions happen on page load.
        this.fetchLast50Entries();
        setInterval(this.fetchRecentEntries, 1000);
    },
    methods: {
        async fetchRecentEntries() {
            const response = await fetch(apiEndpointGetRecent);
            const responseJSON = await response.json();
            const newEntries = responseJSON["data"];

            //console.log("Got this: " + JSON.stringify( newEntries));
            console.log("Got this many results: " + newEntries.length);

            // Add new results.
            for (let i = 0; i < newEntries.length; i++) {
                if (!this.content.some(entry => entry.question === newEntries[i].question && entry.time_generated === newEntries[i].time_generated)) {
                    this.content.push(newEntries[i]);

                    vm.isLoading = false;
                }
            }

            // Sort the results by time generated.
            this.content.sort((a, b) => (a.time_generated > b.time_generated) ? 1 : ((b.time_generated > a.time_generated) ? -1 : 0))

            // Remove the oldest results if we have 50 answers.
            if (this.content.length >= 50) {
                for (let i = 0; i < this.content.length - 50; i++) {
                    this.content.shift();
                }
            }

        },
        async fetchLast50Entries() {
            // Used at page load to get the last 50 results.
            const gResponse = await fetch(apiEndpointGet50);
            const gObject = await gResponse.json();
            //console.log("Got this last 50: " + JSON.stringify( gObject));
            this.content = gObject["data"];
            for (let i=0; i < this.content.length; i++){
                this.content[i].expanded = false;
            }

            vm.isLoading = false;
        },
        forceAnUpdate() {
            // Used to force the page to re-render when clicking on large results to show/hide all of the answer.
            this.$forceUpdate();
        }
    }
})

const clearAllEntries = async () => {
    // Clears all data on the page and in the firestore.
    vm.isLoading = true;
    await fetch(apiEndpointClearEntries);
    vm.content = [];
    vm.isLoading = false;
}

const generate50NewItems = async (maxRandomNumber) => {
    // Sends 50 requests to the Server cloud function to create a new result.
    vm.isLoading = true;
    for (let i = 0; i < 50; i++) {
        await generate1NewItem(maxRandomNumber);
    }
}

const generate1NewItem = async (maxRandomNumber) => {
    // Asks the Server cloud function to generate a new result.
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