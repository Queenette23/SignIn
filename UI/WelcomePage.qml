import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {
    Rectangle {

        Rectangle {
            anchors.fill: parent

            Image {
                sourceSize: Qt.size(parent.width, parent.height)
                fillMode: Image.PerserveAspectCrop
                anchors.centerIn: parent
                source: "./images/tiger3.jpg"
            }

        }

        Text {
            anchors.centerIn: parent
            text: username + ", you have been signed"
            font.pixelSize: 16
            color: "white"
        }
    }
}
