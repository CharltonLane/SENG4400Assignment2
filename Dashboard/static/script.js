'use strict';

window.addEventListener('load', function () {

    console.log("Hello World!");

});

const apiEndpoint = "/getNewEntries"

const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        content: 'Loading...'
    },
    created (){
        this.timer = setInterval(this.fetchNewEntries, 1000);
    },
    methods: {
        async fetchNewEntries () {
            const gResponse = await fetch(apiEndpoint);
            const gObject = await gResponse.json();
            this.content = gObject;
        }
    }

})
