import React from "react";
import ShelterList from "../Components/SheltersList";
import { ShelterService } from "../Services/ShelterService";
import { PageSection, PageSectionVariants, Text, TextContent } from "@patternfly/react-core";


type SheltersViewProps = {
    shelterService: ShelterService;
}


export default class SheltersView extends React.Component<SheltersViewProps> {

    public render() {
        return (
            <React.Fragment>
                <PageSection variant={PageSectionVariants.light}>
                    <TextContent>
                        <Text component="h1">Shelters</Text>
                        <Text component="p">Our shelters</Text>
                    </TextContent>
                </PageSection>
                <PageSection>
                    <ShelterList shelterService={this.props.shelterService}/>
                </PageSection>
            </React.Fragment>
        );
    }

}
