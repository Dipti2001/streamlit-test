import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

def main():
    st.header("WebRTC live video stream demo")

    # Create a start/stop button
    start_button = st.button('Start Camera')
    stop_button = st.button('Stop Camera')

    if start_button:
        # Use session state to manage the stream status
        st.session_state['is_streaming'] = True

    if stop_button:
        # Turn off the stream
        st.session_state['is_streaming'] = False

    # Check if we should display the streamer or not
    if 'is_streaming' not in st.session_state:
        st.session_state['is_streaming'] = False

    if st.session_state['is_streaming']:
        # Start the WebRTC streamer
        webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV)

    else:
        # Display a message when the stream is not running
        st.write("Camera is off. Click 'Start Camera' to turn it on.")

if __name__ == "__main__":
    main()
