import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { routes } from './app.routes';

// import { AppComponent } from './app.component';
// // import { AppRoutingModule } from './app-routing.module';
// import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
// import { AuthInterceptor } from './auth/auth.interceptor';
// import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
// import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
// import { provideRouter } from '@angular/router';
// import { routes } from './app.routes';


// import { LoginComponent } from './login/login.component';
// import { AdminDashboardComponent } fro m './admin-dashboard/admin-dashboard.component';
// import { SuperAdminDashboardComponent } from './super-admin-dashboard/super-admin-dashboard.component';


export const appConfig: ApplicationConfig = {
  providers: [
    // provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
    provideAnimationsAsync(),
    // HttpClientModule,
    // provideForms(), // Les services de formulaire

    // {
    //   provide: HTTP_INTERCEPTORS,
    //   useClass: AuthInterceptor,
    //   multi: true
    // }
  ]
};


// export const appConfig: ApplicationConfig = {
//   providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes)]

// };