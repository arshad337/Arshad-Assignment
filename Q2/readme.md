Yes, Django signals run in the same thread as the caller. We can confirm this by printing the thread IDs in both the calling function and the signal handler

Explaination:
The thread ID is obtained using threading.get_ident(). Both the calling function and the signal handler print the same thread ID, proving that they run in the same thread.