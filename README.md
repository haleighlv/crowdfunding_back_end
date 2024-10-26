# Crowdfunding Back End
Haleigh Vinicombe

## Planning:
### Concept/Name
A Hand Up

A website for people without access to mental health treatment to crowdfund the funds to enable them to access treatment.

### Intended Audience/User Stories
Intended audience: People with a mental health condition who are unable to access treatment due to costs.

- As a user I would like to be able to sign up for an account so that I can create a project or make a pledge.
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
| /projects | GET | Returns all projects | N/A | 200 OK | N/A |
| /projects | POST | Creates a new crowdfunding project | { "title", "description", "goal", "image"} | 201 Created | Must be an existing user and logged in |
| /projects/:id| GET | Returns the project with ID as specified | N/A | 200 OK | N/A |
| /projects/:id | PUT | Updates the project with ID as specified | { "title", "description", "image" } | 200 OK | Must be an existing user who owns project and logged in |
| /projects/:id | DELETE | Deletes the project with the ID as specified | NA | 200 OK | Must be an the specified user who created the project and is logged in or admin |
| --- | --- | --- | --- |--- |--- |
| /pledges | POST | Creates a new pledge for project | Pledge object | 201 Created | Must be an existing user own project and is logged in |
| /pledges/:id | GET | Returns the pledge with ID as specified | N/A | 200 OK | N/A |
| /pledges/:id | PUT | Updates the pledge with ID as specified | { "amount", "anonymous" } | 201 created | Must be an existing user who made the pledge and is logged in |
| /pledges/:id | DELETE | Deletes the pledge with ID as specified | N/A | 200 OK | Must be an existing user who made the pledge and is logged in |
| --- | --- | --- | --- |--- |--- |
| /users | GET | Returns all users | N/A | 200 OK | Admin |
| /users | POST | User signs up | { "username", "email", "password" } | 201 Created | N/A |
| /users/:id | PUT | Updates the user with ID as specified | { "username", "email", "first_name", "last_name", "password" } | 200 OK | Must be an existing user who is logged in or admin |
| /users/:id | DELETE | Deletes the user with the ID as specified as well as any items or bids currently active | N/A | 200 OK | N/A | Must be an the specified user who is logged in or admin

### DB Schema
https://github.com/haleighlv/crowdfunding_back_end/blob/main/DBSchema_Updated2.png

### Link to deployed app
https://haleigh-v-handup-13142a7a1a60.herokuapp.com

Insomnia - Local GET endpoint
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/local-GET-project%20id.png

Insomnia - Heroku GET endpoint
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/heroku-GET-project-id.png

Insomnia - Local POST endpoint
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/local-POST-project.png

Insomnia - Heroku POST endpoint
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/heroku-POST-project.png

Insomnia - Local AUTH TOKEN
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/local-AUTHTOKEN-return.png

Insomnia - Heroku AUTH TOKEN
https://github.com/haleighlv/crowdfunding_back_end/blob/933d29f9a71d584f5bec775a41e801aaded062a1/Screenshots/heroku-AUTHTOKEN-%20return.png

### Registering a new users and creating a new project

### REGISTER USER
- Endpoint: POST /users/
- Action: Create new user account
- Required data: username (unique), email address, password

1. Send a POST request to /users/ with the above required data in JSON format.
2. Ensure the Content-Type header is set to application/json.
3. If successful, confirmation of the user created will be displayed.

### OBTAIN AN AUTHENTICATION TOKEN
- Endpoint: POST /api-auth-token/
- Action: Authenticate and receive token for future requests
- Required data: username, password

1. Send a POST request to /api-token-auth/ with the above required data in JSON format.
2. Ensure the Content-Type header is set to application/json.
3. If successful, you'll receive an authentication token which is need to authenticate future requests.

### CREATE A NEW PROJECT
- Endpoint: POST /projects/
- Action: Create a new project
- Authorisation: Include your token under "Auth" with the prefix "Token"
- Content type: application/json
- Required data: project title, description, funding goal, image URL, is_open if open to pledges otherwise falese, date created (Usually auto generatated by the server).

1. Send a POST request to /aprojects/ with the above required data in JSON format.
2. Ensure the Content-Type header is set to application/json.
3. Include your authorisation token under "Auth".
4. If successful, a response confirming the details of your project will be displayed.