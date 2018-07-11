# Variable Parameter
+ 默认参数

```
def test_defargs(one, two = 2):
   print 'Required argument: ', one
   print 'Optional argument: ', two

test_defargs(1)
# result:
# Required argument: 1
# Optional argument: 2

test_defargs(1, 3)
# result:
# Required argument: 1
# Optional argument: 3
```

+  $*args 和 **Kwargs$
	+  $*args$ 使用方法
		+ 包含一个必须的参数

		```
        def test_args(first, *args):
   		print 'Required argument: ', first
   		for v in args:
     		 print 'Optional argument: ', v

		test_args(1, 2, 3, 4)
		# result:
		# Required argument: 1
		# Optional argument:  2
		# Optional argument:  3
		# Optional argument:  4
        ```
	+  $**kwargs$ 使用方法
		+ 同时包含一个必须的参数和*args列表

        ```
        def test_kwargs(first, *args, **kwargs):
   			print 'Required argument: ', first
   		for v in args:
      		print 'Optional argument (*args): ', v
   		for k, v in kwargs.items():
      		print 'Optional argument %s (*kwargs): %s' % (k, v)

		test_kwargs(1, 2, 3, 4, k1=5, k2=6)
		# results:
		# Required argument:  1
		# Optional argument (*args):  2
		# Optional argument (*args):  3
		# Optional argument (*args):  4
		# Optional argument k2 (*kwargs): 6
		# Optional argument k1 (*kwargs): 5
        ```