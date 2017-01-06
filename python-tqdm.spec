%global modname tqdm

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        4.10.0
Release:        2%{?dist}.1
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


%prep
%autosetup -n %{modname}-%{version}


%build
%py2_build


%install
%py2_install


%check
%{__python2} setup.py test

%files -n python2-%{modname}
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/


%changelog
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
