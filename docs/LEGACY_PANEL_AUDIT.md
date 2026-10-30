# İncelenen ek dosya: `heatwatch_panel(2).zip`

**Durum: Eski/alternatif panel olarak değerlendirilmelidir; güncel model veri seti olduğuna ilişkin kanıt yok.** Bu kontrol 30 Ekim 2026 tarihinde kullanıcı tarafından paylaşılan `panel_building_winter.csv` üzerinden yapılmıştır.

## Doğrudan ölçülenler

| Kontrol | Sonuç |
|---|---:|
| Satır sayısı | 264.251 |
| Benzersiz `bbl10` | 74.299 |
| Hedef kışlar | 2021, 2022, 2023, 2024, 2025 |
| 2025 hedef kışındaki bina sayısı | 74.299 |
| 2025 hedef kışında `y_any=1` oranı | %36,67 |
| Hiç geçmiş şikâyeti olmayan satır (`hist_total=0`) | 0 |
| Tekrarlanan (`bbl10`,`target_winter`) çifti | 0 |
| Eksik `y_repeat` | 110.779 |

Sütunlar: `bbl10`, `target_winter`, `y_any`, `y_ge3`, `prev_cnt`, `prev_any`, `hist_total`, `hist_winters_with`, `y_repeat`.

`y_repeat` yalnızca `prev_any=1` olan satırlarda tanımlanmış görünüyor; dolayısıyla eksik değerleri otomatik sıfıra çevirmek yanlış olur. Tüm panel satırlarının `hist_total>0` olması, geçmişte şikâyet almış bina seçimine işaret ediyor.

## Güncel raporla fark

Güncellenen HeatWatch raporu, evreni 183.417 HPD kayıtlı bina olarak tanımlıyor ve 2025–26 test kışında şikâyet görülme oranını %17,45 olarak raporluyor. Bu CSV ise 2025 hedef kışında yalnızca 74.299 bina içeriyor ve `y_any` oranı %36,67. Bu iki rakam **doğrudan karşılaştırılabilir aynı evren değil**.

Önceki çalışmada şikâyet geçmişine göre seçilmiş bina evreninin daha sonra tüm HPD kayıtlı binalara genişletildiği raporda ifade edilmiş. Bu CSV, o eski yaklaşımın bir çıktısı olabilir, fakat kaynak notebook olmadan sürüm kimliği kesin doğrulanamaz.

## Kullanım kararı

1. **Aktif model verisi olarak kullanmayın.** Son dönem eğitim/test metriklerini yeniden üretmek için bu CSV yeterli değil.
2. Dosyayı özel bir çalışma yedeğinde tutun; genel GitHub deposuna yüklemek zorunda değilsiniz.
3. `bbl10` bina kimliği olduğu için kamuya açık paylaşım ihtiyacını ve olası bina bazlı damgalama riskini gözden geçirin.
4. Gerçek son model verisini ve özgün eğitim/notebook kodlarını arkadaşınızdan istemeye devam edin.
5. İleride tarihsel geliştirme sürecini belgelemek isterseniz bu açıklamayı depoda tutabilirsiniz. Ancak eski CSV'nin **son modelin veri seti olmadığı** net biçimde yazılmalıdır.

> Not: Bu kontrol, model eğitimi veya 2026–27 risk listesinin doğrulanması anlamına gelmez.
