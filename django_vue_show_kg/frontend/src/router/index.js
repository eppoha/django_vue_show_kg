import {createWebHistory, createRouter} from "vue-router";
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import PeopleList from '@/views/PeopleList'
import PeopleDetail from '@/views/PeopleDetail'
import TestParam from '@/views/TestParam'
import SearchPeople from '@/views/SearchPeople'
// import SearchPeople from '@/components/SearchPeople'
// import ShowAll from '@/components/ShowAll'
const routes = [
  {
    path: '/',
    name: 'index',
    component: index
  },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/PeopleList',
      name: 'PeopleList',
      component: PeopleList
    },
    {
        path: '/PeopleDetail',
        name: 'PeopleDetail',
        component: PeopleDetail
      },
      {
        path: '/TestParam',
        name: 'TestParam',
        component: TestParam
      },
      {
        path: '/SearchPeople',
        name: 'SearchPeople',
        component: SearchPeople
      },
    
    // {
    //   path: '/SearchPeople',
    //   name: 'SearchPeople',
    //   component: SearchPeople
    // },
    // {
    //   path: '/ShowAll',
    //   name: 'ShowAll',
    //   component: ShowAll
    // },

  ]

  const router = createRouter({
    // https://next.router.vuejs.org/guide/essentials/history-mode.html
    history: createWebHistory(),
    routes,
});

export default router;