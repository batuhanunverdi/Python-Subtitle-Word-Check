import pysrt as ps

subs = ps.open("a.srt")
SubsLength = len(subs)
subArrays = []
knownWords = []
with open("C:/Users/MBU/Desktop/Bilinen.txt", "r") as file:
    for x in file:
        x = x.strip('\n')
        knownWords.append(x)
unKnownWords = []
sentenceList = []
reSubs = []
sentence = ""


for subLength in range(SubsLength):
    subs[subLength].text = "".join(s for s in subs[subLength].text if s not in ("?", ".", ";", ":", "!", '"', "-", ",")
                                   ).lower().split()
    subArrays.append(subs[subLength].text)

for subArray in subArrays:
    for word in subArray:

        if word not in knownWords:
            unKnownWords.append(word)
            reWord = "<font color='red'>"+word+"</font>"+" "
            sentence += reWord
        else:
            reWord = (word+" ")
            sentence += reWord
    sentenceList.append([sentence])
    sentence = ""

for subLength in range(SubsLength):
    subs[subLength].text = "".join(sentenceList[subLength])

subs.save('b.srt', encoding='utf-8')
