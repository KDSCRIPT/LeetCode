
#My Answer(Time Limit Exceeded)
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        idx=0
        l=[]
        for person in people:
            count=0
            for flower in flowers:
                if person>=flower[0] and person<=flower[1]:
                    count+=1
            l.append(count)
        return l
#The best answer I found in Leetcode(Chatgpt+Leetcode)
def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for i in range(len(people)):
            events.append([people[i],1,i])
        for flower in flowers:
            events.append([flower[0], 0])
            events.append([flower[1], 2])
        events.sort(key=lambda x: (x[0], x[1]))
        ret = [0] * len(people)
        blooms = 0
        for event in events:
            if event[1] == 0:
                blooms += 1
            elif event[1] == 2:
                blooms -= 1
            else:
                person_index = event[2]
                ret[person_index] = blooms
        return ret