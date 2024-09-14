# App server

This contains server code to run the confetti cannon. It can be used in situations where the VIAM SDK is not available, such as through Flutter (the VIAM flutter SDK is not currently working on any platform except iOS).

Run this as a web app, then share the port over the internet using [ngrok](https://ngrok.com) or [Local tunnel](https://theboroer.github.io/localtunnel-www/).

You will need to copy the `.env.example` file to `.env` and set the relevant values.