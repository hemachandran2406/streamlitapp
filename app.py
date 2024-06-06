import streamlit as st

# Set Content Security Policy (CSP) headers
# st.set_option('browser.serverAddress', '0.0.0.0')  # Allow connections from any host
st.set_option('server.cors', True)  # Enable Cross-Origin Resource Sharing (CORS)
st.set_option('server.enableCSP', True)  # Enable Content Security Policy (CSP)

# Configure CSP headers
st.set_option('server.csp', {
    'frame-src': ['https://app.powerbi.com']
})


st.title('Simple Streamlit App')
st.write('This is a simple Streamlit app embedded in a Power BI custom visual.')

if st.button('Click me'):
    st.write('Button clicked!')

