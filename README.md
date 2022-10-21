# WEBZOS

### Tezos on-chain website viewer

### By [Eyal Gruss](https://eyalgruss.com) ([@eyaler](https://twitter.com/eyaler))

Deploy and view eternal websites on the Tezos blockchain that will live as long as Tezos does (i.e. forever!)

Web: [wbtz.github.io](https://wbtz.github.io)

Code: [https://github.com/wbtz/wbtz.github.io](https://github.com/wbtz/wbtz.github.io)

Uses: [tzkt.io](https://tzkt.io), [better-call.dev](https://better-call.dev), [smartpy.io](https://smartpy.io) and [ZTML](https://github.com/eyaler/ztml)

### Instructions

#### Simple deployment:
- Edit HTML here: [smartpy.io/ide?code=...](https://smartpy.io/ide?code=eJxNUEFugzAQvCPxh@3JoEr0WlUhqkqp2kuoEqoovVgGTGLJ2Mi7OdDX14aiZn2wd3Zsz4waRusIcBCOxgkEAo5xFFarBSIcZfNjMcExK6whJ1pKn@IIfHWyB86VUcR5glL36yDUhQYNOTjGWBxt7l6roj59lgHd@n6eamHOuTShHyQJaC_CoaT8Sv1jAEmRlttj@fJdHTYPS@fhxnaT34tqV5e7Gqo3OFVfe_C8w0ddwnu5L@No_nbVErRlQWdwcSWlMWsmkshtz5GcMuckCMrCeUzSNF38qx4YyWHUwnMZGEugjHdsxCA5__P67J8UXcc9hRK2hMXS_4Bm_DYY9Kn4OwHn2EojnLJJeju_z9fQPfwLaWh4oA--)
- Media can be encoded inline as Base64 data URLs
- Minify your code (e.g. reduce whitespace) to save money
- Run and deploy contract

#### Advanced deployment with compression:
- Use [ZTML Colab](https://bit.ly/ztml1) to compress HTML (important: tick `raw`), or plain text 
- Copy the output hex dump from the last cell
- Paste inside here: [smartpy.io/ide?code=...](https://smartpy.io/ide?code=eJxNkE1rAkEMhu@C_yG3maGw9FwQLP1aoVaxK7anMO7O4sDOB5Mc1F_vTO2iye1N8uZJrIshMZDTieMJNAHF6aRkO2gi2Jn9OZCkWL0Ez0m3rJ6mE8jRmR4QrbeMKMkM_VgocWA34MEcYQaifvuB1@1yDat3@F1tN1A3y0_4bp43zeLrA3aLpobHo7gNF7OqGJe1@xMbkqNfRZxslEqpK6TtQbBxcdC5S4APDNZnLK@dQfwHmmcb3XWYW1iK60VC3a740@_pKWPnmaIjtcbrZINU9_WH2fiZLF8AtjZcnQ--)
- Run and deploy contract

Note: total (compressed) size is currently limited to 32 kB

#### Viewing:
- Access your website by appending [wbtz.github.io](https://wbtz.github.io) with [?]() or [#]() followed by the originated KT address
- For example: [wbtz.github.io?KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz](https://wbtz.github.io?KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz) (Try it!)
- This will load the HTML from the contrat storage via [tzkt.io](https://tzkt.io/KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz/storage) or [better-call.dev](https://better-call.dev/mainnet/KT1JnLUUE9idUYnjRu8hgChEnZWGa8FfauRz/storage)
