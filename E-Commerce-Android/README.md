## About the App

E-Commerce is an Android shopping app that connects to a backend through a REST API. It is Part 1 of a four-part e-commerce project (Android, Flutter, MERN web app, and JavaFX desktop app) that shares one system.

## Features

- Sign up and sign in
- Product browsing with search and an image slider
- Cart, address entry, order summary, and payment screens
- Navigation drawer
- Shows the exact reason for an order return
- Google Maps integration

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Java |
| Architecture | MVVM with Android Architecture Components (LiveData, ViewModel, ViewBinding) |
| Networking | Retrofit, OkHttp3, GSON |
| Dependency Injection | Koin |
| Local Storage | Room Persistence Library |
| Image Loading | Glide |
| UI | Material Components, RecyclerView, GridView, CardView, Fragments, SearchView, SwipeRefresh, BottomSheet |
| Build Tool | Gradle |

## Architecture

The app follows the **MVVM (Model-View-ViewModel)** pattern. The UI observes data exposed by ViewModels, and a repository layer handles the network and local data sources.

## Package Structure

```
dev.atharvakulkarni.e_commerce
├── data
│   ├── model        # Model classes
│   ├── network/api  # Retrofit API endpoints
│   └── repository   # Single source of data
├── ui
│   ├── main         # Main screen, adapters, ViewModel
│   └── details      # Detail screen and ViewModel
└── utils            # Utility classes
```

## Screenshots

See the `Screenshots` folder for the Home, Cart, Address, Order Summary, Payment, Sign In, and Sign Up screens.
