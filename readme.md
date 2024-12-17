# The User Management System Final Project 🎉✨🔥

## Course Reflection

This comprehensive course has been an immersive journey into the world of data programming with Python and web development. The focus on hands-on projects has honed my critical problem-solving skills, enabling me to address complex information system requirements effectively. 

### Key Learnings:
- **Proficiency in Python Programming**: Worked extensively with data sources like CSV files, SQL databases, and REST-based web services.
- **Professional Competencies**:
  - Adherence to industry standards and code best practices.
  - Mastery of Git for version control, Agile development principles, and object-oriented programming.
- **Collaborative Problem Solving**: Engaged in version-controlled workflows, resolving real-world challenges in a professional environment.

This course has equipped me with the technical expertise and professional acumen required to thrive in competitive fields like data programming and web development.


## Project Documentation

### Key Features:
- **User Profile Management**: Enhanced functionality for managing user profiles, including verification and role updates.

### Closed QA Issues:
1. **Issue 1**: Token Not Verified for Second User  
   - **Description**: Token verification failed for the second user due to improper session handling before sending the verification email.  
   - **Solution**: Ensured session commit occurs before sending the email.  
   - [Closed Issue](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/app/services/user_service.py#L70)

2. **Issue 2**: Admin Email Verification Issue  
   - **Description**: Admin user token verification failed due to misaligned expiration handling.  
   - **Solution**: Updated role-specific conditions for token handling.  
   - [Closed Issue](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/app/services/user_service.py#L170)

### New Tests:
Ten new test cases were written to ensure robust functionality and enhance code coverage. These include:
1. [Test Case 1: Update user profile success](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L15)
2. [Test Case 2: Update user profile not found](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L26)
3. [Test Case 3: Update user profile partial update](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L36)
4. [Test Case 4: Update user profile invalid field](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L47)
5. [Test Case 5: Update professional status success](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L57)
6. [Test Case 6: Update professional status not found](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L66)
7. [Test Case 7: Update professional status no change](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L76)
8. [Test Case 8: Update user profile with special characters](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L85)
9. [Test Case 9: Update user profile empty data](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L95)
10. [Test Case 10: Update professional status toggle](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/tests/test_services/test_userprofile_management.py#L106)

### New Feature:
- **User Profile Management**  
  - Implemented in `user_service.py` to allow users to manage their profiles seamlessly.  
  - [Feature Link](https://github.com/GxPatel/user_management/blob/cc9ea632eb8acb8b8020d004fc4d0521fec070b5/app/services/user_service.py#L209)


## Docker Deployment

The application has been containerized and deployed on Docker Hub for easy distribution and scalability.  
**DockerHub Repository**: [WIS Club API](https://hub.docker.com/repository/docker/gxpatel/wis_club_api/general)
