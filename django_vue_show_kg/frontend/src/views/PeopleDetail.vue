<!--  frontend/src/views/ArticleDetail.vue  -->

<template>

    <div v-if="data !== null" >
        <div>
            <h1 id="name">{{ data.name }}</h1>
            <p id="subtitle">
                {{ data.wuli }} {{ data.desc }} {{ data.text_all }}
            </p>
            
        </div>
        
    </div>

    

</template>

<script>

    import axios from 'axios';

    export default {
        name: 'PeopleDetail',
        data: function () {
            return {
                data: null,
                id:this.$route.query.id
            }
        },
        mounted() {
            console.log("id=",this.$route.query.id)
            axios
                .get('/api/peoplepeople/' + this.$route.query.id)
                .then(response => (this.data = response.data))
        },
        
    }
</script>

