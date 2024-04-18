<template>
  <!-- frontend\src\views\SearchPeople.vue -->
    <div>
      <div class="search-div">
        <el-icon><Search />Input</el-icon>
        <div><input v-model="queryName" placeholder="Please input"></input></div>
        <div><button type="primary" @click="SearchFunc">Search</button></div>
    </div>
    
        <client-only>
      <el-table :data="queryResults" style="width: 100%" height="250">
        <el-table-column prop="name" label="姓名" width="100" ></el-table-column>
        <el-table-column prop="gender" label="性别" width="100" />
        <el-table-column prop="number" label="编号" width="100" />
        <el-table-column prop="wuli" label="武力值" width="100" />
        <el-table-column prop="zhili" label="智力值" width="100" />
        <el-table-column prop="texing1" label="特性1" width="100" />
        <el-table-column prop="texing2" label="特性2" width="100" />
        <el-table-column prop="texing3" label="特性3" width="100" />
        <el-table-column prop="bishaji" label="必杀技" width="100" />
        <el-table-column prop="yili" label="义理" width="100" />
        <el-table-column prop="xiangxing" label="相性" width="100" />
        <el-table-column prop="zhongzu" label="种族" width="120" />
        <el-table-column prop="img" label="图片" width="100" />
        <el-table-column prop="figure" label="形象" width="120" />
      </el-table></client-only></div>
    </template>
    
    <script>
    // eslint-disable-next-line
     /* eslint-disable */
    import {searchData} from "@/router/search.js"
    export default {
    data: function(){
            return {
              queryName:"", // chaxun
              queryResults: [],
              
            }
        },
        methods: {
            SearchFunc() {
                console.log("search field:", this.queryName)
                const params ={'name':this.queryName} 
                console.log("search params:", params)
                searchData(params).then(res=>{
                    console.log("search res:", res)
                    this.queryResults.length = 0  // clear
                    this.queryResults = res.res
                    console.log("===search data res:",this.queryResults )
                })
            },
        },
    
    }
    </script>
    