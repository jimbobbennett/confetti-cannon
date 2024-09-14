# Confetti cannon Flutter code

This code can be added to a Flutter app to give a simple app with one button that fires the confetti cannon. You will need to have the [`app-server`](../app-server/) running, as this uses that to connect.

The aim of this code is to be shared as a Pieces snippet, so folks can add it to a new flutter app.

This is the description for the code snippet:


This code sample can be used to launch the Pieces confetti cannon at FlutterCon!

To use this:
1. Install Pieces, including the extension for your preferred IDE and your browser
2. Save this code snippet to Pieces
3. Create a new flutter app
4. Add the HTTP package:

    `flutter pub add http`

5. Replace the code in `main.dart` with this code snippet
6. Ask the Pieces team for the key, and update `key` with the value
7. Ask the Pieces team to prime a new confetti launcher
8. Run the Flutter app and press the Confetti button!

This has been tested with Chrome, iOS, Android and macOS.

For macOS, you will need to add:

<key>com.apple.security.network.client</key>
    <true/>

to your `macos/Runner/DebugProfile.entitlements` and `macos/Runner/ReleaseProfile.entitlements` files.