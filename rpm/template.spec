Name:           ros-indigo-rqt-logger-level
Version:        0.3.12
Release:        0%{?dist}
Summary:        ROS rqt_logger_level package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_logger_level
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-rospkg
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-catkin

%description
rqt_logger_level provides a GUI plugin for configuring the logger level of ROS
nodes. rqt_logger_level takes over `wx`-based tool [[rxloggerlevel]].

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jul 24 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.12-0
- Autogenerated by Bloom

* Sat May 02 2015 Aaron Blasdel <ablasdel@gmail.com> - 0.3.11-0
- Autogenerated by Bloom

