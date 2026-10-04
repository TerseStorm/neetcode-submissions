class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visitedList = []
        edgeQueue = []
        level = 1
        edgeQueue = self.addToQueue(beginWord, wordList, edgeQueue, visitedList, level+1)
        while edgeQueue:
            curWord, level = edgeQueue.pop(0)
            visitedList.append(curWord)
            print(f"Current Word: {curWord}")
            edgeQueue = self.addToQueue(curWord, wordList, edgeQueue, visitedList, level+1)
            if curWord == endWord:
                return level
        return 0

    def addToQueue(self, curWord, wordList, edgeQueue, visitedList, level):
        for word in wordList:

            distance = self.overlayDistance(curWord, word)
            if distance == 1 and not (word in edgeQueue or word in visitedList):
                edgeQueue.append([word, level])
        return edgeQueue



    def overlayDistance(self, str1, str2):
        distance = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1
        return distance