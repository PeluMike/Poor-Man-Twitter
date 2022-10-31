const {
    createApp
} = Vue


const url = "http://127.0.0.1:8000"
    // import axios from "axios"

createApp({
    data() {
        return {
            tweetList: [],
            tweets: "",
            name: ""
        }
    },
    methods: {
        submitHandler(e) {
            e.preventDefault()
            var formData = new FormData()
            const config = {}

            formData.append("name", this.name)
            formData.append("tweet", this.tweets)
            if (this.name !== '' && this.tweets !== '') {
                axios.post(`${url}/create/`, formData, config).then((response) => {
                    this.name = ""
                    this.tweets = ""
                    this.fetchTweets()
                }).catch((e) => {
                    console.log(e.message)
                })
            }
        },
        fetchTweets() {
            axios.get(url).then((response) => { this.tweetList = response.data }).catch((e) => {
                console.log('api error!')
            })
        }
    },
    mounted() {
        this.fetchTweets()
    }
}).mount('#app')