import speedtest
st = speedtest.Speedtest()
download = st.download() /1024/1024


upload = st.upload()/1024/1024
ping = st.results.ping

print(f"Dowload speed: {download:.2f} Mpbs")
print(f"Upload speed: {upload:.2f} Mpbs")
print(f"Ping: {ping:.2f} ms")
