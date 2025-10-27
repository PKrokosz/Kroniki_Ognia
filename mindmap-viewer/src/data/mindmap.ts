import { MindNode } from "../lib/types";

export const ROOT_NODE: MindNode = {
  id: "kroniki-ognia",
  title: "Kroniki Ognia — Drzewo",
  content: "Wybierz gałąź, aby zobaczyć dwie warstwy dalej.",
  children: [
    {
      id: "swietosc-ognia",
      title: "Świętość Ognia",
      content: "Rdzeń rytuałów i dogmatów płomieni.",
      children: [
        {
          id: "rytualy",
          title: "Rytuały",
          content: "Opis kluczowych ceremonii.",
          children: [
            { id: "przysiega-plomieni", title: "Przysięga Płomieni" },
            { id: "nocne-czuwanie", title: "Nocne czuwanie" }
          ]
        },
        {
          id: "doktryny",
          title: "Doktryny",
          children: [
            { id: "kodeks-plomienia", title: "Kodeks Płomienia" },
            { id: "proroctwa-zarzy", title: "Proroctwa Żarzy" }
          ]
        }
      ]
    },
    {
      id: "struktury-klasztoru",
      title: "Struktury klasztoru",
      content: "Hierarchia życia codziennego.",
      children: [
        {
          id: "rada-trzech",
          title: "Rada Trzech",
          children: [
            { id: "mistrz-ognia", title: "Mistrz Ognia" },
            { id: "archiwista", title: "Archiwista" }
          ]
        },
        {
          id: "nowicjat",
          title: "Nowicjat",
          children: [
            { id: "sciezka-przypalki", title: "Ścieżka Przypałki" },
            { id: "dni-proby", title: "Dni próby" }
          ]
        }
      ]
    },
    {
      id: "poslannictwo",
      title: "Posłannictwo",
      content: "Misje i wyprawy zwiadowców.",
      children: [
        {
          id: "zwiad",
          title: "Zwiad",
          children: [
            { id: "sieci-sojuszy", title: "Sieci sojuszy" },
            { id: "notatniki-wypraw", title: "Notatniki wypraw" }
          ]
        },
        {
          id: "opieka-nad-plomieniem",
          title: "Opieka nad Płomieniem",
          children: [
            { id: "ogrody-zaru", title: "Ogrody żaru" },
            { id: "krypty-popielne", title: "Krypty popielne" }
          ]
        }
      ]
    },
    // TODO: Uzupełnij resztę gałęzi według mapy myśli
  ]
};
