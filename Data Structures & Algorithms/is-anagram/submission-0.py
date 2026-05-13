class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Freqs ={}
        Freqt={}

        for i in s:
            if i in Freqs:
                Freqs[i]+=1
            else:
                Freqs[i]=1
        for i in t:
            if i in Freqt   :
                Freqt[i]+=1         
            else:
                Freqt[i]=1
        return Freqs==Freqt        