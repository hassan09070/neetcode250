import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.tweets = {}      # userId -> list of (time, tweetId)
        self.following = {}   # userId -> set of followees
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((-self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # include self + followees
        followees = self.following.get(userId, set())
        followees.add(userId)

        for uid in followees:
            if uid in self.tweets:
                for tweet in self.tweets[uid]:
                    heap.append(tweet)

        heapq.heapify(heap)

        feed = []
        for _ in range(min(10, len(heap))):
            feed.append(heapq.heappop(heap)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)