<!--   frontend/src/views/PeopleList.vue   -->
<template>
    
    <div v-for="people in info.results" v-bind:key="people.name" id="people">
        <!-- <div class="people-name">
            {{ people.name }}
        </div> -->
        人物id：{{ people.id }}
        <router-link :to="{ name: 'PeopleDetail', query: { id: people.id}}"
                class="people-name"
        >
            {{ people.name }}
        </router-link>
    </div>
    <div id="paginator">
        <span v-if="is_page_exists('previous')">
            <router-link :to="{ name: 'PeopleList', query: { page: get_page_param('previous') } }">
                Prev
            </router-link>
        </span>
        <span class="current-page">
            {{ get_page_param('current') }}
        </span>
        <span v-if="is_page_exists('next')">
            <router-link :to="{ name: 'PeopleList', query: { page: get_page_param('next') } }">
                Next
            </router-link>
        </span>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                info: '',
                name:'',
                data:'',
                
            }
        },
        mounted() {
            // console.log("id=", this.params.id),
            axios
                .get('/api/peoplepeople/')
                .then(response => (this.info = response.data))
        },
        methods:{
            // 判断页面是否存在
            is_page_exists(direction) {
                if (direction === 'next') {
                    return this.info.next !== null
                }
                return this.info.previous !== null
            },
            // 获取页码
            //get_page_param: function(direction) {
            get_page_param: function(direction) {
                try {
                    let url_string;
                    switch (direction) {
                        case 'next':
                            url_string = this.info.next;
                            break;
                        case 'previous':
                            url_string = this.info.previous;
                            break;
                        default:
                            return this.$route.query.page
                    }

                    const url = new URL(url_string);
                    return url.searchParams.get('page')
                }
                catch (err) {
                    return
                }
            },
            // 获取人物列表数据
            get_people_data: function () {
                let url = '/api/peoplepeople';
                const page = Number(this.$route.query.page);
                if (!isNaN(page) && (page !== 0)) {
                    url = url + '/?page=' + page;
                }

                axios
                    .get(url)
                    .then(response => (this.info = response.data))
            }
        },
        watch: {
            // 监听路由是否有变化
            $route() {
                this.get_people_data()
                console.log("this.get_people_data():", this.get_people_data())
            }
        }
        }
    
</script>

<style>
    #people {
        padding: 10px;
    }

    .people-name {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
    #paginator {
        text-align: center;
        padding-top: 50px;
    }

    a {
        color: black;
    }

    .current-page {
        font-size: x-large;
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
    }
</style>