

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />

<p align="center">
  <a href="https://github.com/Artists-Forum-NITK/AF_Website">
    <img src="https://github.com/Artists-Forum-NITK/AF_Website/blob/master/mysite/static/images/af-small.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Artists' Forum</h3>

  <p align="center">
    <a href="http://example.com/"><strong>  Artists' Forum Website »</strong></a>
    <br>
    <br>
    <a href="https://af.nitk.ac.in/">Website Link</a>
    ·
    <a href="issues-url">Report Bug</a>
    ·
    <a href="https://github.com/Artists-Forum-NITK/AF_Website/issues/new">Request Feature</a>
  </p>
</p>

## Models In the Website

### Content Regulation
- Member
- Image
- Event
- Art
- Blog
- Udaan
- Comment
- Gallery

### User Account Management
- Account
- Recruitment Applicant
- My Account Manager
- Volunteer
- Registration

## Functionalities 

- The content in terms of team members' data, images, events, artworks, blog content,etc. can be uploaded via the admin dashboard by the superadmin or the user with admin permissions.

- Appropriate filters in place for the content that is to be displayed on various pages. 

- Dislaying Images corresponding to the events, blogs or Artworks in various sections on the website pages.

- User Account Management interface for recruitments, volunteers and registrations for the club and club events/projects.

- Improved UI/UX with a better theme and template.

- Image Compression for files with a larger size, while preserving the quality/resolution.

- Mailer for the users to get latest updates via email, and for other relevant actions.

- Further implemented features to be based on the requirements specified by the core members.

## Installation Guide 

- Fork the Project and Clone it locally,
- Run the following commands in you teminal:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```
- Now enter `localhost:8000` in the browser.



[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Artists-Forum-NITK/AF_Website/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/artists_forum_nitk/?originalSubdomain=in
[product-screenshot]: https://github.com/Artists-Forum-NITK/AF_Website/blob/master/mysite/static/images/af-small.png
