%global modname tqdm

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        4.47.0
Release:        1%{?dist}
Summary:        A Fast, Extensible Progress Meter

# see PACKAGE-LICENSING for more info
License:        MPLv2.0 and MIT
URL:            https://github.com/tqdm/tqdm
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
tqdm (read taqadum, تقدّم) means "progress" in Arabic.\
\
Instantly make your loops show a smart progress meter - just wrap any iterable\
with "tqdm(iterable)", and you are done!


%description %{_description}


%package -n python2-%{modname}
Summary:        %{summary}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-coverage
BuildRequires:  python-flake8


%description -n python2-%{modname} %{_description}

Python 2 version.



%package -n python36-%{modname}
Summary:        %{summary}
BuildRequires:  python36-devel
BuildRequires:  python36-setuptools


%description -n python36-%{modname} %{_description}

Python 3.6 version.


%prep
%autosetup -n %{modname}-%{version}


%build
%py3_build
%py2_build


%install
%py3_install
mv %{buildroot}%{_bindir}/%{modname} %{buildroot}%{_bindir}/%{modname}-%{python3_version}

%py2_install
mv %{buildroot}%{_bindir}/%{modname} %{buildroot}%{_bindir}/%{modname}-%{python2_version}

# Create symlinks
ln -s ./%{modname}-%{python3-version} %{buildroot}%{_bindir}/%{modname}-3
ln -s ./%{modname}-%{python2-version} %{buildroot}%{_bindir}/%{modname}-2
ln -s ./%{modname}-%{python2-version} %{buildroot}%{_bindir}/%{modname}


%files -n python2-%{modname}
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}
%{_bindir}/%{modname}-2*
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/


%files -n python36-%{modname}
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}-3*
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/


%changelog
* Mon Jun 29 2020 Stephen Gallagher <sgallagh@redhat.com> - 4.47.0-1
- Update to 4.47.0

* Fri Apr 03 2020 Stephen Gallagher <sgallagh@redhat.com> - 4.45.0-1
- Update to 4.45.0
- Install /usr/bin/tqdm only for python2

* Tue May 21 2019 Stephen Gallagher <sgallagh@redhat.com> - 4.10.0-2.3
- Add python36 version

* Thu Jun 01 2017 Stephen Gallagher <sgallagh@redhat.com> - 4.10.0-2.2
- Bump and rebuild to work around bug in Bodhi

* Fri Jan 06 2017 Stephen Gallagher <sgallagh@redhat.com> - 4.10.0-2.1
- Do not use Recommends of pandas and numpy on EPEL 6 and EPEL 7
- Don't build python3 on EPEL

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.10.0-2
- Rebuild for Python 3.6

* Sun Nov 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Mon Oct 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.9.0-1
- Update to 4.9.0

* Tue Aug 16 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.8.3-1
- Update to 4.8.3

* Fri Jul 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.7.6-1
- Update to 4.7.6

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.7.4-1
- Initial package
