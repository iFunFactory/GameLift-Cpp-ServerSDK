This repository is for easy deployment of the gamelift cpp server sdk.
-----------------------------------------------------------------------

To generate a rpm package, run sudo ./build_rpm.sh.

You may need to install packages to meet its dependency requirement.
In this case, please see our another repos containing RPMs required by GameLift.

https://github.com/iFunFactory/RPMs-for-AmazonLinux


Below is the original README.md


# GameLiftServerSdk C++
## Documention
You can find the official GameLift documentation [here](https://aws.amazon.com/documentation/gamelift/).
## Minimum requirements:
* Either of the following:  
  * Microsoft Visual Studio 2012 or later  
  * GNU Compiler Collection (GCC) 4.9 or later
* CMake version 2.8 or later
## Building the SDK
### Out of source build
To build the server sdk, all you must do is the following:  
Linux -
```sh
mkdir out
cd out
cmake ..
make
```

Windows -
```sh
mkdir out
cd out
cmake -G "Visual Studio 14 2015 Win64" ..
msbuild ALL_BUILD.vcxproj /p:Configuration=Release
```

This SDK is known to work with these CMake generators:
* Visual Studio 14 2015 Win64
* Visual Studio 12 2013 Win64
* Visual Studio 11 2012 Win64
* Unix MakeFiles

### CMake options
#### BUILD_FOR_UNREAL

Optional variable to build the SDK for use with Unreal Engine. Set variable to 1 to create an Unreal build. Default setting is false.
With this option enabled, all dependencies are built statically and then rolled into a single shared object library.
```sh
cmake -DBUILD_FOR_UNREAL=1 ..
```

#### BUILD_SHARED_LIBS

Optional variable to select either a static or dynamic build. Default setting is static. Set variable to 1 for dynamic.

```sh
cmake -DBUILD_SHARED_LIBS=1 ..
```

#### GAMELIFT_USE_STD

Optional variable to choose whether or not to use the C++ STD when building. Default setting is true. 

```sh
cmake -DGAMELIFT_USE_STD=1 ..
```

#### USE_SYSTEM_BOOST

Option to choose whether to use the Boost library already installed on the system. Default is off.
```sh
cmake -DUSE_SYSTEM_BOOST=1 ..
```

#### USE_SYSTEM_PROTOBUF

Option to choose whether to use the protobuf library already installed on the system. Default is off.
```sh
cmake -DUSE_SYSTEM_PROTOBUF=1 ..
```

#### USE_SYSTEM_SIOCLIENT

Option to choose whether to use the socket.io client library already installed on the system. Default is off.
```sh
cmake -DUSE_SYSTEM_SIOCLIENT=1 ..
```
