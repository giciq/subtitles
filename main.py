import assemblyai as aai

aai.settings.api_key = "???"
transcriber = aai.Transcriber()

for i in range(1, n):
    print("Started "+str(i)+"\n")
    transcript = transcriber.transcribe("./video"+str(i)+".mp4")

    text = transcript.export_subtitles_srt()
    f = open("subs"+str(i)+".srt", "w")
    f.write(text)
    f.close()
