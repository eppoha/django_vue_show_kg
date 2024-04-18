<template>
    <div>
        id 为        {{ userId }}
    </div>
</template>

<script>

    export default {
        name: 'TestParam',
        data: function () {
            return {
                id: this.$route.query.num,
                userId:this.$route.query.num,
            }
        },
        created() {
            const userId = this.$route.query.num;
            console.log("userId=",userId); // 应该能够看到传递的参数值，而不是undefined
        
        },
        mounted() {
            console.log("id=",this.$route.query.num)
            // axios
            //     .get('/api/peoplepeople/' + this.$route.params.id)
            //     .then(response => (this.data = response.data))
        },
        
    }
</script>