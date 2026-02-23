Name:              redisbloom
Version:           8.6.0
Release:           1%{?dist}
Summary:           Probabilistic data structures

# License breakdown:
# - redisbloom: AGPL-3.0-only (tri-licensed: RSALv2/SSPLv1/AGPLv3, using AGPLv3)
# - deps/readies, deps/bloom: BSD-3-Clause
# - deps/RedisModulesSDK, deps/t-digest-c: MIT
License:           AGPL-3.0-only AND MIT AND BSD-3-Clause
URL:               https://github.com/RedisBloom/RedisBloom
Source0:           https://github.com/dariaguy/redisbloom-rpm/releases/download/v8.6.0/redisbloom-8.6.0.tar.gz

BuildRequires:     make
BuildRequires:     cmake
BuildRequires:     gcc
BuildRequires:     gcc-c++
BuildRequires:     python3
BuildRequires:     openssl-devel

Provides:          bundled(RedisModulesSDK)
Provides:          bundled(readies)
Provides:          bundled(t-digest-c)

Supplements:       redis

%global redis_modules_dir %{_libdir}/redis/modules
%global redis_modules_cfg %{_sysconfdir}/redis/modules
%global libname          redisbloom.so
%global cfgname          redisbloom.conf

%description
RedisBloom adds a set of probabilistic data structures to Redis, including
Bloom filter, Cuckoo filter, Count-min sketch, Top-K, and t-digest.
Using this capability, you can query streaming data without needing to
store all the elements of the stream.


%prep
%autosetup -p1

mv deps/RedisModulesSDK/LICENSE LICENSE-RedisModulesSDK
mv deps/readies/LICENSE         LICENSE-readies
mv deps/t-digest-c/LICENSE.md   LICENSE-t-digest-c


%build
make build


%install
install -Dpm755 bin/linux-*-release/%{libname} %{buildroot}%{redis_modules_dir}/%{libname}
install -Dpm640 %{cfgname}                     %{buildroot}%{redis_modules_cfg}/%{cfgname}


%files
%license LICENSE.*
%license licenses/AGPLv3.txt
%doc *.md
%attr(0640, redis, root) %config(noreplace) %{redis_modules_cfg}/%{cfgname}
%{redis_modules_dir}/%{libname}


* Wed Feb 23 2026 Daria Guy <daria.guy@redis.com> - 8.6.0-1
- Initial package for RedisBloom 8.6.0