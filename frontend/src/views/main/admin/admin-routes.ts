export const adminRoutes = [
  {
    path: 'users',
    redirect: 'users/all',
  },
  {
    path: 'users/all',
    component: () =>
      import(/* webpackChunkName: "main-admin-users" */ './users/AdminUsers.vue'),
  },
  {
    path: 'users/edit/:id',
    name: 'main-admin-users-edit',
    component: () =>
      import(/* webpackChunkName: "main-admin-users-edit" */ './users/EditUser.vue'),
  },
  {
    path: 'users/create',
    name: 'main-admin-users-create',
    component: () =>
      import(/* webpackChunkName: "main-admin-users-create" */ './users/CreateUser.vue'),
  },
  {
    path: 'chapters',
    redirect: 'chapters/all',
  },
  {
    path: 'chapters/all',
    component: () =>
      import(/* webpackChunkName: "main-admin-chapters" */ './chapters/AdminChapters.vue'),
  },
  {
    path: 'chapters/create',
    component: () =>
      import(/* webpackChunkName: "main-admin-chapters" */ './chapters/CreateChapter.vue'),
  },
];
