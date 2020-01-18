
%global qt_module qtdoc

#define prerelease

Summary: Main Qt5 Reference Documentation
Name:    qt5-%{qt_module}
Version: 5.9.7
Release: 1%{?dist}

License: GFDL
Url:     http://www.qt.io
Source0: http://download.qt.io/official_releases/qt/5.9/%{version}/submodules/%{qt_module}-opensource-src-%{version}.tar.xz
BuildArch: noarch
%global _qt5_qmake %{_bindir}/qmake-qt5

BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-doctools
BuildRequires: qt5-qtbase-doc

%description
QtDoc contains the main Qt Reference Documentation, which includes
overviews, Qt topics, and examples not specific to any Qt module.


%prep
%setup -q -n %{qt_module}-opensource-src-%{version}


%build
%{qmake_qt5}
make docs %{?_smp_mflags}

%install
make install_docs INSTALL_ROOT=%{buildroot}


%files
%doc LICENSE.FDL
%{_qt5_docdir}/qtdoc.qch
%{_qt5_docdir}/qtdoc/


%changelog
* Thu Feb 07 2019 Jan Grulich <jgrulich@redhat.com> - 5.9.7-1
- Update to 5.9.7
  Resolves: bz#1564004

* Fri Oct 06 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- Update to 5.9.2
  Resolves: bz#1482779

* Mon Aug 28 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.1-1
- Update to 5.9.1
  Resolves: bz#1482779

* Wed Jan 11 2017 Jan Grulich <jgrulich@redhat.com> - 5.6.2-1
- Update to 5.6.2
  Resolves: bz#1384818

* Tue Aug 30 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-10
- Increase build version to have newer version than in EPEL
  Resolves: bz#1317401

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1
  Resolves: bz#1317401

* Thu Apr 07 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-2
- Initial version for RHEL
  Resolves: bz#1317401

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Wed Feb 24 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.9.rc
- Fix release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.8.rc
- Update to final RC

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.7
- Update RC release

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.4
- use %%qmake_qt5 (and hack around %%_qt5_qmake noarch issue)

* Fri Dec 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.3
- fix merge

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.2
- Official beta release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 29 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-2
- BR: qt5-qhelpgenerator

* Wed Jun 24 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2-rc
- Update for official RC1 released packages

* Wed Jun 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-0.1-rc
- Qt 5.5.0 RC1

* Wed Jun 03 2015 Jan Grulich <jgrulich@redhat.com> -5.4.2-1
- 5.4.2

* Tue Feb 24 2015 Jan Grulich <jgrulich@redhat.com> 5.4.1-1
- 5.4.1

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-1
- 5.4.0 (final)

* Fri Nov 28 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.2.rc
- 5.4.0-rc

* Mon Oct 20 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.1.beta
- 5.4.0-beta

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-1
- 5.3.2

* Tue Jun 17 2014 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jan Grulich <jgrulich@redhat.com> 5.3.0-1
- 5.3.0

* Wed Feb 05 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-1
- 5.2.1

* Thu Dec 12 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-1
- 5.2.0

* Fri Dec 06 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.11.rc1
- BR: qt5-qtbase-devel

* Mon Dec 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.10.rc1
- 5.2.0-rc1

* Thu Oct 24 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.2.beta1
- 5.2.0-beta1

* Thu Oct 10 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.1.alpha
- 5.2.0-alpha

* Mon Sep 30 2013 Rex Dieter <rdieter@fedoraproject.org> 5.1.1-2
- License: GFDL

* Sun Sep 22 2013 Rex Dieter <rdieter@fedoraproject.org> 5.1.1-1
- Initial packaging
