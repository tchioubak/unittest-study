# unittest-study
Try and study unittest

# test_stupid.py
Tested with python 3.9
```text
python -V
Python 3.9.16
```

Results are :
```text
python -m unittest test_stupid.py
got msg what
got msg what
got msg hard
.got msg what
got msg what
got msg hard
Fgot msg what
got msg what
Egot msg what
got msg what
.got msg what
got msg what
got msg soft
happy of this little chat
.
======================================================================
ERROR: test_hard_n3 (test_stupid.TestStupid)
not OK because of exit
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib64/python3.9/unittest/mock.py", line 1336, in patched
    return func(*newargs, **newkeywargs)
  File "/home/infratst/appli/connexion/gits/private/questions/test_stupid.py", line 20, in test_hard_n3
    stupid.StupidDialog().dialog()
  File "/home/infratst/appli/connexion/gits/private/questions/stupid.py", line 10, in dialog
    sys.exit(1)
SystemExit: 1

======================================================================
FAIL: test_hard_exit_n3 (test_stupid.TestStupid)
not OK because of call_count
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib64/python3.9/unittest/mock.py", line 1336, in patched
    return func(*newargs, **newkeywargs)
  File "/home/infratst/appli/connexion/gits/private/questions/test_stupid.py", line 42, in test_hard_exit_n3
    self.assertEqual(mock_input.call_count, 3)
AssertionError: 4 != 3

----------------------------------------------------------------------
Ran 5 tests in 0.005s

FAILED (failures=1, errors=1)
```
