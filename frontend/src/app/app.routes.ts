import { AppComponent } from './app.component';
import { Routes } from '@angular/router';

export const routes: Routes = [

    // { 
    //     path: '', 
    //     loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) 
    //   },
    //   { 
    //     path: 'superadmin', 
    //     loadChildren: () => import('./superadmin/superadmin.module').then(m => m.SuperadminModule) 
    //   },
    //   { 
    //     path: 'category', 
    //     loadChildren: () => import('./category/category.module').then(m => m.CategoryModule) 
    //   },
    //   { 
    //     path: 'product', 
    //     loadChildren: () => import('./product/product.module').then(m => m.ProductModule) 
    //   },
    //   { 
    //     path: 'cashier', 
    //     loadChildren: () => import('./cashier/cashier.module').then(m => m.CashierModule) 
    //   },
    //   { 
    //     path: 'admin', 
    //     loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) 
    //   }


    // { 
    //     path: '', 
    //     component: AppComponent,
    //     children: [
    //       { path: '', redirectTo: 'auth', pathMatch: 'full' },
    //       { path: 'auth', loadChildren: () => import('./auth/auth.module').then(m => m.AuthModule) },
    //       { path: 'superadmin', loadChildren: () => import('./superadmin/superadmin.module').then(m => m.SuperadminModule) },
    //       { path: 'category', loadChildren: () => import('./category/category.module').then(m => m.CategoryModule) },
    //       { path: 'product', loadChildren: () => import('./product/product.module').then(m => m.ProductModule) },
    //       { path: 'cashier', loadChildren: () => import('./cashier/cashier.module').then(m => m.CashierModule) },
    //       { path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }
    //     ]
    //   }
];
