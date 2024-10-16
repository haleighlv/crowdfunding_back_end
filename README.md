# Crowdfunding Back End
Haleigh Vinicombe

## Planning:
### Concept/Name
A Hand Up

A website for people without access to mental health treatment to crowdfund the funds to enable them to access treatment.

### Intended Audience/User Stories
Intended audience: People with a mental health condition who are unable to access treatment due to costs.
.
- As a user with a mental health condition, I want to be able to set up a crowdfunding project to raise funds for treatment.
- As a user I would like to tell my story and add photos to my project.
- As a user who has started a crowdfunding project I would like to see how much my project has earnt.
- As a user I would like to be abe to update my details delete my account.

- As a supporter who has an interest in mental health and treatments, I would like to be able to read peoples stories and the treatment they are looking to undertake.
- As a supporter who has the means to support others, I would like to support those in need to access treatment.
- As a supporter, I want the process to be straightforward and I would like to see a list of all pledges I have made.
- As a supporter, I would like to be able to update my details or delete my account.

- As a super user, I want to be able to see a list of all projects.
- As a super user, I want to be able to see a list of all users.
- As a super user, I want to be able to see a list of all pledges.


### Front End Pages/Functionality
- Home page
    - Link to sign up/user profile 
    - Link to create project
    - List of top projects by pledge
    - Selection of recently created projects
- User sign up page
    - Page for users to sign up to enable them to create a project or bid on a project
- User profile page
    - A list of all my uploaded projects
    - A list of all my pledges
    - My personal details (name, email, mobile)
    - A way to delete my account
- Create project page
    - Form to collect details of project and amount needed to be raised
    - Ability to include description and photos
-  Project detail page
   -  Description about project including photos
   -  A list of pledges for this project
   -  If I am a supporter, a way to create a new pledge for this project
 
 API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | --- | --- | --- |--- |--- |
| /projects | GET | Returns all projects | N/A | 200 | N/A |
| /projects | POST | Creates a new crowdfunding project | Project object | 201 | Must be an existing user and logged in |
| /projects/:id| GET | Returns the project with ID as specified | N/A | 200 | N/A |
| /projects/:id | PUT | Updates the project with ID as specified | Project object | 201 | Must be an existing user who owns project and logged in |
| --- | --- | --- | --- |--- |--- |
| /pledges | POST | Creates a new pledge for project | Pledge object | 201 | Must be an existing user own project and is logged in |
| /pledges/:id | GET | Returns the pledge with ID as specified | N/A | 200 | N/A |
| /pledges/:id | PUT | Updates the pledge with ID as specified | Project object | 201| Must be an existing user who made the pledge and is logged in |
| /pledges/:id | DELETE | Deletes the pledge with ID as specified | N/A | 200 | Must be an existing user who made the pledge and is logged in |
| --- | --- | --- | --- |--- |--- |
| /users | GET | Returns all users | N/A | 200 | N/A |
| /users | POST | User signs up | User object | 201 | N/A |
| /users/:id | PUT | Updates the user with ID as specified | User object | 200 | Must be an existing user who is logged in or admin |
| /users/:id | DELETE | Deletes the user with the ID as specified as well as any items or bids currently active | N/A | 200 | N/A | Must be an the specified user who is logged in or admin

### DB Schema
https://github.com/haleighlv/crowdfunding_back_end/blob/main/DBSchema_Updated2.png