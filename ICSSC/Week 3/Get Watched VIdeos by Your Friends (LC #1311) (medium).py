# https://leetcode.com/problems/get-watched-videos-by-your-friends/

from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        q = [id]
        v = set()
        h = {0: [id]}
        cl = 0
        s = set()

        while level not in h:
            
            if q:
                c = q.pop(0)
                v.add(c)
            else:
                q += list(s)
                cl += 1
                s.clear()
            
            for ch in friends[c]:
                if ch not in v:
                    s.add(ch)
                    if cl in h:
                        h[cl].append(ch)
                    else:
                        h[cl] = [ch]
        
        f = h[level]
        wh = {}
        for fr in f:
            for vid in watchedVideos[fr]:
                if vid in wh:
                    wh[vid] += 1
                else:
                    wh[vid] = 1

        return sorted(wh.keys(), key= lambda x: (wh[x], x))