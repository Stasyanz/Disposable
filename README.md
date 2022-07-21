![release badge](https://img.shields.io/github/v/release/Stasyanz/Disposable?display_name=release)
[![Docker Image CI](https://github.com/Stasyanz/Disposable/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Stasyanz/Disposable/actions/workflows/docker-image.yml)
## A simple disposable one-time messages service.

When one adds a new message, he gets a one-time link to it. 

Once link is seen by anyone its being deleted.

### Use case

You want to be sure no one is reading your chat with your friend. 

You create a one-time message and give you friend a link using you chat app.

Once friend reads the message, its deleted. 

If your friend can't read the message that means someone has already read your message.

### Getting started

`docker-compose up`

Use `.env` file to set up your own environment variables.
