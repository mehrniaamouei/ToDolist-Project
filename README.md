# ToDolist-Project 📝🚀

## Overview

**ToDolist-Project** is a comprehensive project and task management tool designed to help you organize all aspects of your projects effortlessly. With this application, you can create, edit, and delete projects, and add multiple tasks to each project. You can also update the status of tasks, edit their details, or remove them when they are no longer needed.  

## 🔹 Special Focus on Tasks

Tasks in this system have special features that make project management more effective:  
- **Title & Description:** Each task has a concise title and a detailed description to explain the work.  
- **Status:** Tasks can have a status of `todo`, `doing`, or `done` ✅, allowing you to easily track progress.  
- **Deadline:** Assign deadlines 📅 to tasks to ensure timely completion and better prioritization.  

This structure ensures that progress is always visible, deadlines are respected, and no task is overlooked.  

## ⚙️ Configuration & Limits

To prevent overload, the **maximum number of projects** and **tasks per project** can be configured via the `.env` file. The project also includes error handling and validation to guarantee that all entered data is correct and reliable.  

## 🌟 Features

- Create, edit, and delete projects 🏗️  
- Add, edit, and remove tasks for each project 🗂️  
- Change task status to track progress ✅  
- Assign deadlines to tasks ⏰  
- View a list of all projects and their tasks 📋  
- Configurable limits via `.env` file ⚡  


## ⚠️ Deprecation Notice

The Command Line Interface (CLI) is no longer a core feature of this project and its use is discouraged.  
All new features and developments will only be available through the API.  
Please refer to the [API endpoints](./app/api/routers.py) for usage and future development.
