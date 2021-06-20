---
driveId: 1RDxB6372smxcfzK-MNZ0QYRSInbKlyP5/preview
---

## Self-Assessment

Under construction! Feel free to check back later.

## [Chosen Artifact](https://github.com/Shaun-Richardson/CS499-Capstone/tree/gh-pages/OriginalArifact)

My artifact comes from the CS-260 Data Structures and Algorithms course at SNHU. In its simplest terms the project loads a bids csv file and can then do several small tasks such as display all of the data, find a predetermined item from the data, or delete the predetermined item from the data. However, none of the data is stored, and upon close, nothing is saved. 

## Code Review

{% include googleDrivePlayer.html id=page.driveId %}


## [Enhancement One: Software Design and Engineering](https://github.com/Shaun-Richardson/CS499-Capstone/tree/gh-pages/EnhancementOne) 

My artifact comes from the CS-260 Data Structures and Algorithms course at SNHU. In its simplest terms the project loads a bids csv file and can then do several small tasks such as display all the data, find a predetermined item from the data, or delete the predetermined item from the data. However, none of the data is stored, and upon close, nothing is saved. 

The reason I chose this artifact for my ePortfolio is because it has clear room for improvement and to me seemed like a good way to showcase some of the techniques, I learned in a more recent course CS-340 client/server development. Specifically, converting a program to a new language and allowing it to become interactable with its database. This artifact shows that I can work with new tools and convert projects to a new language if that language provides a benefit to the overall project and accomplishes the course outcome [CS-499-04] by following industry-standard organization and techniques. In this case converting this project to Python allows for the projects planned future enhancements, database communication, and front-end development while not losing any of the functionality of the initial artifact.  

Reflecting on this enhancement I learned more than I expected thanks to a few hiccups along the way. Initially I wanted to use the VDI (A virtual environment) that was provided within the previous course that allowed us to complete assignments with a preloaded environment that had all the tools pre-installed. I learned that it was not possible to regain this access but that ended up working in my favor, academically, because I learned how to setup MongoDB, Python, and Jupyter Notebook on my own local environment. The process of converting my project to a new language was much more straight forward and I did not run into any issues. Overall, the conversion to Python allowed the artifact to be written in a language where I felt confident enough to provide a working, interactable, database and a new redesigned front-end.  

## [Enhancement Two: Algorithms and Data Structure](https://github.com/Shaun-Richardson/CS499-Capstone/tree/gh-pages/EnhancementTwo)

My artifact comes from the CS-260 Data Structures and Algorithms course at SNHU. In its simplest terms the project loads a bids csv file and can then do several small tasks such as display all the data, find a predetermined item from the data, or delete the predetermined item from the data. However, none of the data is stored, and upon close, nothing is saved. 

I chose this artifact because it had clear room for improvement. Since this artifact was used as a learning tool all the components of the project were done in the same .cpp file. Again, being a learning tool, this artifact lacked any particular security and gave users direct access to many parameters that should have been private. With that in mind I improved this artifact by moving the main algorithms of the artifact to a Python C.R.U.D module that allows creation, reading, updating, deleting, and now security. These features accomplish the course outcomes of [CS-499-03] and [CS-499-05]. One of the main additions is this security feature that allows users to connect to the database, but only if they have been giving explicit permission to that database, by the administration of said database. Lastly, with the overall move to Python from C++ I was able to showcase my ability to convert the algorithms of my artifact into another language that will provide further benefits to the program. One such benefit is the ability for my algorithms to interact with the database and produce front-end components (Example: a DataTable). Rather than the algorithms of the artifact that only interacted with a user loaded .csv file, but changes could not be recorded or saved due to the limitations of the program. 

Reflecting on this enhancement I learned that porting or refactoring code, especially in a new language, can be challenging. I had to spend a considerable amount of time learning about my new IDE Jupyter Notebook. As I stated previously, I had to setup my environment from scratch and that led to me having to learn all the libraries I needed to download using a tool I was unfamiliar with; PIP the package manager for Python. Once I had all my needed libraries converting my algorithms from the initial artifact was straight forward. Overall, I learned how to convert algorithms into a new language that, when tested, interacts with a connected database, and learned how to secure those connections between the application/database.  


## [Enhancement Three: Databases](https://github.com/Shaun-Richardson/CS499-Capstone/tree/gh-pages/EnhancementThree)

My artifact comes from the CS-260 Data Structures and Algorithms course at SNHU. In its simplest terms the project loads a bids csv file and can then do several small tasks such as display all the data, find a predetermined item from the data, or delete the predetermined item from the data. However, none of the data is stored, and upon close, nothing is saved. 

From a database perspective this artifact had a lot of room for improvement. It was a large data set, stored in an excel .csv, and when loaded was hard to read by the user. For my improvements I converted the .csv file into a MongoDB with authorization which ultimately increased the security of the project. Next, I was able to create a dashboard using the Dash framework along with Pymongo that not only looks a lot easier to read but incorporates the main components of the artifact. My new dashboard provides the user with a data table that has been loaded from the MongoDB database using a username/password, an additional pie chart allows users to visualize the breakdown of bids (in view) based on department, and data table controls that allow users to sort, search, and remove rows. These new enhancements show that I am capable of learning and reusing new technologies, relative to my own experience, and that I can update old content/databases to an easier-to-read interactive format. 

Reflecting on this enhancement I learned a lot about MongoDB, Python, the Dash framework, and the challenges that come along with them. Many of the hurdles I faced were setting up my environment to run MongoDB, as I had never used it outside of the virtual environment in the previous course. Once it was all set up, I had no issues with importing my .csv database into MongoDB, but I had to learn how to setup authentication again using a combination of previous course notes/screenshots and google. As for the interactive front-end, Dash.Plotly has some wonderful documentation that allowed me to accomplish my results posted in the link to the enhancement. Overall, I was able to accomplish a complete project utilizing a MongoDB database, Python algorithms, and a front-end using the Dash.Plotly framework that is modularized in such a way that I could easily plug in completely new databases and authentication creating a new project from this in minutes.

