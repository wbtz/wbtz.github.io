# WEBZOS

### Tezos on-chain website viewer

by [Eyal Gruss](https://eyalgruss.com)

Deploy and view eternal websites on the Tezos blockchain that will live as long as Tezos does (i.e. forever!)

web: [wbtz.github.io](https://wbtz.github.io) or [webzos.page.tez](https://webzos.tez.page)

code: [https://github.com/wbtz/wbtz.github.io](https://github.com/wbtz/wbtz.github.io)

uses: [tzkt.io](https://tzkt.io), [better-call.dev](https://better-call.dev) and [smartpy.io](https://smartpy.io)

<b>Instructions:</b>

Edit and deploy your website: [smartpy.io/ide?code=...](https://smartpy.io/ide?code=eJxNUMtqxDAMvPsr1JMTSrPXUpKwsO25PRTKnoyTKBuDH8FSKOnX107SsroIj8bSzBg3h8hATkeeV9AENAshequJ4Au7n0AFzdUleI665_JFQKoBR1DKeMNKFYR2PPBc39snaNKiamFjqepWRlJhVMTR@FsRpZSifnh9v3xeP95gYmdbUecGVvtbgz4_UQ@pOWQN_aQjITcLj0_PCWTDFtv6tHdRnw5yF4a1FdewxKyCDCNMGDER9kkibrfS_fJfb5ZfZSvFrrxM9s0IktHNViflEnxgMD459tqhUrvXc_Knh0ElBhdyj@pYm@PZ4LtYjkQyrKhHr6MJxZ0KeGz@8i7FL0RTfQ8-)

Notes: 
- Storage is currently limited to 32 kB per website
- You can use base64 data URLs for media (keep it lean)
- Minify your code (e.g. reduce whitespace)

Access your website by appending the current domain with ? or # followed by the originated KT address, for example:
[wbtz.github.io?KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz](https://wbtz.github.io?KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz) (try it!)