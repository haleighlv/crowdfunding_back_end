# Crowdfunding Back End
Haleigh Vinicombe

## Planning:
### Concept/Name
A Hand Up

A website for people without access to mental health treatment to crowdfund the funds to enable them to access treatment.

### Intended Audience/User Stories
- As someone with a mental health condition, I want to be able to set up a crowdfunding project to raise funds for treatment.

- As someone who has the means to support others, I would like to support those in need to access treatment

- As someone making a pledge, I want the process to be straightforward.

### Front End Pages/Functionality
- Home page
    - Link to create project
    - Link to browse current projects
    - Selection of recently created projects
- User sign up page
    - Page for users to sign up to enable them to create a project or bid on a project
- Create project page
    - Form to collect details of project and amount needed to be raised
- Browse page
    - Ability to browse all current projects
-  Bid/Pledge page
    - Form for user to make a pledge for a project

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | --- | --- | --- |--- |--- |
| /projects | GET | Returns all projects | N/A | 200 | N/A |
| /projects | POST | Creates a new crowdfunding project | Project object | 201 | Must be an existing user and logged in |
| /projects/:id| GET | Returns the project with ID as specified | N/A | 200 | N/A |
| /projects/:id | PUT | Updates the project with ID as specified | Project object | 201 | Must be an existing user who owns project and logged in |
| --- | --- | --- | --- |--- |--- |
| /pledges | POST | Creates a new pledge for project | Pledge object | 201 | Must be an existing user own project and is logged in |
| /pledges/:id | GET | Returns the pledge with ID as specified | N/A | 200 | N/A |
| /pledges/:id | DELETE | Deletes the pledge with ID as specified | N/A | 200 | Must be an existing user who made the pledge and is logged in |
| --- | --- | --- | --- |--- |--- |
| /users | GET | Returns all users | N/A | 200 | N/A |
| /users | POST | User signs up | User object | 201 | N/A |
| /users/login | POST | User logs in | User object | 200 | N/A |
| /users/:id | PUT | Updates the user with ID as specified | User object | 200 | Must be an existing user who is logged in or admin |
| /users/:id | DELETE | Deletes the user with the ID as specified as well as any items or bids currently active | N/A | 200 | N/A | Must be an existing user who is logged in or admin

### DB Schema
(https://github.com/haleighlv/crowdfunding_back_end/blob/6b5f2c9865fb66f8437909e1f5465c5980c61805/DBSchema.png)