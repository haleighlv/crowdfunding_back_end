# Crowdfunding Back End
Haleigh Vinicombe

## Planning:
### Concept/Name
Stationery Destash

A website for people to upload and sell their collectable stationery and stickers.

### Intended Audience/User Stories
As a stationery addict who has a tendency to buy excess collectible stationery, I want a place that I am able to sell or give away my excess items. I'd also like the opportunity to purchase items I missed out on or are unique.

### Front End Pages/Functionality
- Home page
    - Link to list items
    - Link to browse items on offer
    - Selection of recently uploaded items
- User sign up page
    - Page for users to sign up to enable them to either upload or buy items from the site
- Upload items page
    - Form to collect details of item and image
- Browse page
    - Ability to browse all items submitted
-  Bid/Pledge page
    - Form for user to make a bid on an item 

### API Spec
PROJECTS = ITEMS FOR SALE
PLEDGES = BIDS/OFFERS FOR SALE

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | --- | --- | --- |--- |--- |
| /projects | GET | Returns all items | N/A | 200 | N/A |
| /projects | POST | Creates a new item for offers/sale | Project object | 201 | Must be an existing user and logged in |
| /projects/:id| GET | Returns the item with ID as specified | N/A | 200 | N/A |
| /projects/:id | PUT | Updates the item with ID as specified | Project object | 201 | Must be an existing user who owns item and logged in |
| --- | --- | --- | --- |--- |--- |
| /pledges | POST | Creates a new bid/offer for item | Pledge object | 201 | Must be an existing user who does not own the item and is logged in |
| /pledges/:id | GET | Returns the bid/offer with ID as specified | N/A | 200 | N/A |
| /pledges/:id | DELETE | Deletes the bid/off with ID as specified | N/A | 200 | Must be an existing user who made the bid/offer and is logged in |
| --- | --- | --- | --- |--- |--- |
| /users | GET | Returns all users | N/A | 200 | N/A |
| /users | POST | User signs up | User object | 201 | N/A |
| /users/login | POST | User logs in | User object | 200 | N/A |
| /users/:id | PUT | Updates the user with ID as specified | User object | 200 | Must be an existing user who is logged in or admin |
| /users/:id | DELETE | Deletes the user with the ID as specified as well as any items or bids currently active | N/A | 200 | N/A | Must be an existing user who is logged in or admin

### DB Schema
(https://github.com/haleighlv/crowdfunding_back_end/blob/main/*.png)