%{?scl:%scl_package osgi-resource-locator}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:          %{?scl_prefix}osgi-resource-locator
Version:       1.0.1
Release:       7.1%{?dist}
Summary:       OSGi resource locator bundle
License:       CDDL or GPLv2 with exceptions
Url:           http://hk2.java.net/
# svn export https://svn.java.net/svn/hk2~svn/tags/osgi-resource-locator-1.0.1
# tar czf osgi-resource-locator-1.0.1-src-svn.tar.gz osgi-resource-locator-1.0.1
Source0:       %{pkg_name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-master-pom package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: %{?scl_prefix_maven}felix-osgi-compendium
BuildRequires: %{?scl_prefix_maven}felix-osgi-core

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix_maven}maven-plugin-bundle

BuildArch:     noarch

%description
OSGi resource locator bundle - used by various API providers that
rely on META-INF/services mechanism to locate providers.

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -n %{pkg_name}-%{version} -q
cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-jar-plugin']" "<version>2.4</version>"
%pom_remove_parent

%mvn_file :%{pkg_name} %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 1.0.1-7.1
- Import latest from Fedora

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.0.1-6
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.1-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 05 2013 gil cattaneo <puntogil@libero.it> 1.0.1-2
- switch to XMvn
- minor changes to adapt to current guideline

* Sat Aug 25 2012 gil cattaneo <puntogil@libero.it> 1.0.1-1
- initial rpm
