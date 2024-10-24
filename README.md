# Library Management System

## Overview
The Library Management System is a Python-based application designed with clean code architecture principles, promoting modularity, readability, and maintainability. This system allows users to efficiently manage a collection of books in a library, providing functionalities for adding and removing books, registering users, borrowing and returning books, and viewing both available and borrowed books.

By employing a structured design that separates concerns into distinct modules, the application enhances collaboration and simplifies future enhancements or debugging. This approach not only ensures that the codebase is easy to navigate but also fosters best practices in software development, making it suitable for both educational purposes and real-world applications.


## Features
- **Book Management**: Add and remove books from the library.
- **User Management**: Register users (both regular and admin) and manage their borrowing activities.
- **Borrowing System**: Users can borrow and return books easily.
- **Book Availability**: View currently available and borrowed books in the library.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/eliashossain001/Library-Management-System
```
2. Navigate to the directory
   ```bash
   cd Library-Management-System
   ```
## Usages
To run the application, execute the following command:
   ```bash
   cd python main.py

## Folder Structure Explanation

- **entities/**: This folder contains all the entities used in the application. 
  - `book.py` defines the structure and behavior of books in the system.
  - `user.py` handles user details, including regular users and admin users.

- **use_cases/**: This folder contains the core business logic. 
  - `library.py` manages all the interactions between books and users, such as adding books, registering users, and managing borrow/return operations.

- **main.py**: The entry point of the program where the system is initialized, books and users are created, and operations like borrowing and returning books are demonstrated. It serves as the controller that binds all the components together.


## Clean Code Architecture

The project follows the Clean Code Architecture principles to ensure that the code remains modular, easy to understand, and extendable:

- **Modularization**: The code is broken down into separate modules with distinct responsibilities, improving clarity and maintainability.

- **Readable variable and function names**: Descriptive and self-explanatory variable and function names are used to convey their purposes clearly, ensuring the code is easy to follow.

- **Separation of concerns**: Each class or module has a specific role, like:
  - Handling books (`BookInformation`)
  - Managing users (`UserRecord`, `AdminUser`)
  - Executing library operations (`LibraryProperty`)
  
  This separation makes the code easier to maintain and update.

```


