Name:           ros-jade-rqt-top
Version:        0.4.6
Release:        0%{?dist}
Summary:        ROS rqt_top package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_top
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-psutil
Requires:       ros-jade-python-qt-binding >= 0.2.19
Requires:       ros-jade-rospy
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
BuildRequires:  ros-jade-catkin

%description
RQT plugin for monitoring ROS processes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Mar 02 2017 Dan Lazewatsky <dan@lazewatsky.com> - 0.4.6-0
- Autogenerated by Bloom

* Fri Feb 03 2017 Dan Lazewatsky <dan@lazewatsky.com> - 0.4.5-0
- Autogenerated by Bloom

* Fri Jan 27 2017 Dan Lazewatsky <dan@lazewatsky.com> - 0.4.4-0
- Autogenerated by Bloom

* Wed Nov 02 2016 Dan Lazewatsky <dan@lazewatsky.com> - 0.4.3-0
- Autogenerated by Bloom

* Tue Mar 08 2016 Dan Lazewatsky <dan@lazewatsky.com> - 0.3.13-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Dan Lazewatsky <dan@lazewatsky.com> - 0.3.12-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Dan Lazewatsky <dan@lazewatsky.com> - 0.3.11-0
- Autogenerated by Bloom

