## 我现在是完全不知道怎么写



发生什么事了
我是ssss

## 设计一个数据库操作类，可以通过这个类对数据库进行操作
class OpDataBase



git push -u origin main


## flask 的文件操作
``` python
f = request.files["file"]
```
使用这个来获得请求的文件对象，这里面放的参数应该是文件表单input 的name
['__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parse_content_type', 'close', 'content_length', 'content_type', 'filename', 'headers', 'mimetype', 'mimetype_params', 'name', 'save', 'stream']
是这个对象具有的属性

**可以通过save保存文件**
```  python
# f save
            # Save the file to a destination path or file object.  If the
                # destination is a file object you have to close it yourself after the
                # call.  The buffer size is the number of bytes held in memory during
                # the copy process.  It defaults to 16KB.

                # For secure file saving also have a look at :func:`secure_filename`.

                # :param dst: a filename, :class:`os.PathLike`, or open file
                #     object to write to.
                # :param buffer_size: Passed as the ``length`` parameter of
                #     :func:`shutil.copyfileobj`.

                # .. versionchanged:: 1.0
                #     Supports :mod:`pathlib`.

            f.save(dst=f.name)  # dst 参数表示文件上传后的名称
```